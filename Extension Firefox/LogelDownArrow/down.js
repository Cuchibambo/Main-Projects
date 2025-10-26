// from : 
// <a href="#" class="back-to-top d-flex align-items-center justify-content-center active">
//     <svg class="svg-inline--fa fa-arrow-up" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-up" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg=""><path fill="currentColor" d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2V448c0 17.7 14.3 32 32 32s32-14.3 32-32V141.2L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"></path></svg><!-- <i class="fa-solid fa-arrow-up"></i> Font Awesome fontawesome.com -->
// </a>
// to :
// <a class="back-to-top d-flex align-items-center justify-content-center active" href="#CDTID_info">
//     <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" data-fa-i2svg="" class="svg-inline--fa fa-arrow-down"><path fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><!-- <i class="fa-solid fa-arrow-up"></i> Font Awesome fontawesome.com -->
// </a>
(function () {
  // Wait until DOM is ready
  document.addEventListener("DOMContentLoaded", () => {
    // Find the existing "back-to-top" link
    const link = document.querySelector("a.back-to-top");

    if (!link) return; // If not found, do nothing

    // Update the href
    link.setAttribute("href", "#CDTID_info");

    // Replace SVG contents
    link.innerHTML = `
      <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img"
           xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"
           data-fa-i2svg="" class="svg-inline--fa fa-arrow-down">
        <path fill="currentColor"
          d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160
             c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8
             224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7
             L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0
             s-12.5 32.8 0 45.3l160 160z"></path>
      </svg>
      <!-- <i class="fa-solid fa-arrow-up"></i> Font Awesome fontawesome.com -->
    `;
  });
})();