use fon::chan::Ch16;
use fon::{Audio, Frame};
use twang::noise::White;
use twang::ops::Gain;
use twang::osc::Sine;
use twang::Synth;

/// First ten harmonic volumes of a piano sample (sounds like electric piano).
const HARMONICS: [f32; 10] = [
    0.700, 0.243, 0.229, 0.095, 0.139, 0.087, 0.288, 0.199, 0.124, 0.090,
];
/// The three pitches in a perfectly tuned A3 minor chord
const PITCHES: [f32; 3] = [220.0, 220.0 * 32.0 / 27.0, 220.0 * 3.0 / 2.0];
/// Volume of the piano
const VOLUME: f32 = 1.0 / 3.0;

// State of the synthesizer.
#[derive(Default)]
struct Processors {
    // White noise generator.
    white: White,
    // 10 harmonics for 3 pitches.
    piano: [[Sine; 10]; 3],
}

fn main() {
    // Initialize audio
    let mut audio = Audio::<Ch16, 2>::with_silence(48_000, 48_000 * 5);
    // Create audio processors
    let mut proc = Processors::default();
    // Adjust phases of harmonics.
    for pitch in proc.piano.iter_mut() {
        for harmonic in pitch.iter_mut() {
            harmonic.shift(proc.white.step());
        }
    }
    // Build synthesis algorithm
    let mut synth = Synth::new(proc, |proc, mut frame: Frame<_, 2>| {
        for (s, pitch) in proc.piano.iter_mut().zip(PITCHES.iter()) {
            for ((i, o), v) in s.iter_mut().enumerate().zip(HARMONICS.iter()) {
                // Get next sample from oscillator.
                let sample = o.step(pitch * (i + 1) as f32);
                // Pan the generated harmonic center
                frame = frame.pan(Gain.step(sample, (v * VOLUME).into()), 0.0);
            }
        }
        frame
    });
    // Synthesize 5 seconds of audio
    synth.stream(audio.sink());

    



    // Convert the fon audio buffer to i16 samples.
    let samples = audio.as_i16_slice().to_vec();

    // Windows default audio device.
    let host = cpal::default_host();

    let device = host
        .default_output_device()
        .expect("No audio output device found");

    println!("Playing through: {}", device.name().unwrap());

    let supported = device
        .default_output_config()
        .expect("No supported output configuration");

    let channels = supported.channels() as usize;

    // The generated audio is 48 kHz stereo.
    let config = cpal::StreamConfig {
        channels: channels as u16,
        sample_rate: cpal::SampleRate(48_000),
        buffer_size: cpal::BufferSize::Default,
    };

    let samples = Arc::new(Mutex::new(samples));
    let position = Arc::new(Mutex::new(0usize));

    let samples_clone = Arc::clone(&samples);
    let position_clone = Arc::clone(&position);

    let stream = device
        .build_output_stream(
            &config,
            move |output: &mut [i16], _| {
                let samples = samples_clone.lock().unwrap();
                let mut position = position_clone.lock().unwrap();

                for frame in output.chunks_mut(channels) {
                    for (channel, sample) in frame.iter_mut().enumerate() {
                        let source_channel = channel.min(1);

                        let index =
                            *position * 2 + source_channel;

                        if index < samples.len() {
                            *sample = samples[index];
                        } else {
                            *sample = 0;
                        }
                    }

                    *position += 1;
                }
            },
            move |err| {
                eprintln!("Audio error: {err}");
            },
            None,
        )
        .expect("Failed to create audio stream");

    stream.play().expect("Failed to start audio stream");

    // Keep the program alive while the 5-second sound plays.
    std::thread::sleep(Duration::from_secs(6));




}