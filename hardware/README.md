* Folder `setupCameraToBackend`

Taking photo from ESP32 cam then it convert into Base64 string 
and added to JSON object to send via HTTP to Async backend to 
get back JSON response object.

* Folder `setupAsync`

Handle async HTTP calls from hardware to the backend vise versa.

* Folder `setupPowerUpPowerDown`

Handle hardware interrupts to trigger ESP32 protection features from
external sources such as Batteries and Weather condition.

* Folder `setupHandMoves`

Usage of Inverse Kinematics algorithms for the Hand movements.

* Folder `setupRoverMoves`

Usage of Hall effect sensor to measure distance and current status.
Control servo motors.

