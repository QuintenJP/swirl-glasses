# Swirl Glasses

A web page that streams animated blue-and-orange swirling eyes to Shining Glasses LED glasses (36 × 12 RGB matrix)
over Bluetooth. Open it at <https://quintenjp.github.io/swirl-glasses/>.

- **Browsers:** Chrome on Android or a computer, or the Bluefy browser on iPhone (Safari has no Web Bluetooth).
- **Streaming:** each Bluetooth packet updates the 8 pixels that are most out of date, so the motion stays continuous.
- **Backup slideshow:** saves one loop of the design to the glasses, which then play it with no phone at about 2 frames/s.
- **Night out:** keeps the screen awake, reconnects automatically, and has a black pocket mode (double-tap to leave).

Close the official app first: the glasses accept one connection at a time.

The protocol comes from the reverse-engineering report in
[aks3310/glasses-eyes](https://github.com/aks3310/glasses-eyes). This is an unofficial personal project,
not affiliated with the glasses' maker or the app's developer.

`scan.py` (Python, `bleak`) only listens for the glasses' Bluetooth advertisements.
