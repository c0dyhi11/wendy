# Wendy
Wendy brings organization as well as dictates logic in Neverland... A place with very little of both!

## Features
* Create Hardware (allow bulk operations)
	* Dynamically assign an IP Address to this system from IPAM
* Create Flavors
* Create Networks
* Provision operating systems onto that hardware (allow bulk operations)
  * Dynamically determine which piece of hardware is optimal to provision to based on requirements (Flavor, Network)
  * Create a dynamic workflow from a template to apply to the hardware
  * Set boot order to PXE (if possible)
  * Power on the server remotely (if possible)
  * Once system has booted disable "allow_pxe"
* Deprovision and Power Off hardware (allow bulk operations)
	* Grab a specific piece of hardware
	* Enable "allow_pxe" on this hardware
	* Create a workflow to "wipe" the system for this hardware
	* Set boot order to PXE (if possible)
	* Power on the server remotely (if possible)
	* The workflow should power off the server one complete