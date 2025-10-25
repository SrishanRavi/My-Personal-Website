/* General website functionality (carousel init + smooth scrolling) */

(function () {
  'use strict'

  // Initialize when DOM is loaded
  window.addEventListener('DOMContentLoaded', () => {
    // Initialize carousel if it exists
    const myCarousel = document.querySelector('#myCarousel')
    if (myCarousel && window.bootstrap && typeof bootstrap.Carousel === 'function') {
      /* eslint-disable no-new */
      new bootstrap.Carousel(myCarousel, {
        interval: 5000,
        wrap: true
      })
    }

    // Add smooth scrolling to navigation links
    document.querySelectorAll('nav a').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href') || ''
        if (href.startsWith('#')) {
          e.preventDefault()
          const targetId = href.substring(1)
          const targetElement = document.getElementById(targetId)
          if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' })
          }
        }
      })
    })
  })
})();