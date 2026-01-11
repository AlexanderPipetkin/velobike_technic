// const CACHE_NAME = 'velobike-v1.0';
// const urlsToCache = [
//   'index.html',
//   'manifest.json',
//   'media/icons/main_icon.png',
//   'media/models/vel.svg',
//   'db/damages.json',
//   'media/vblogo.png',
//   'media/metka.png',
//   'media/icons/main.png',
//   'media/icons/damage.png', 
//   'media/icons/timestamp.png',
//   'media/icons/profile.png',
//   'media/icons/flashlight.png'
// ];

// self.addEventListener('install', function(event) {
//   event.waitUntil(
//     caches.open(CACHE_NAME)
//       .then(function(cache) {
//         return cache.addAll(urlsToCache);
//       })
//   );
// });

// self.addEventListener('fetch', function(event) {
//   event.respondWith(
//     caches.match(event.request)
//       .then(function(response) {
//         if (response) {
//           return response;
//         }
//         return fetch(event.request);
//       }
//     )
//   );
// });