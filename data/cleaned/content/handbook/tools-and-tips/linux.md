---
title: "Linux tools and tips"
description: " Various tools and tips related to Linux laptop usage in GitLab"
---

Linux is available as an alternative to macOS, but is not encouraged due to limited support. By choosing Linux, you accept full responsibility for maintaining your environment and understand that IT does not provide support. There is a #linux channel in Slack for exchanging tips and tricks, but it is not an official helpdesk resource.

The following is a guide to go over the basics of what is recommended for installation to get you up and running as quickly as possible.

- Not everything listed here may apply to your use case.
- This document will not cover the customization desired for your own personal configuration and setup of your desktop/window manager/etc.
- This guide is intended to be very generic. Be aware package names listed here may be have been renamed.
- And as always, there are multiple ways to do many things, so if you have a better preference or are more familiar with another method, feel free to do so and contribute back to this document.

## Basic Setup

Outside of the basics listed [here](/handbook/eta/corporate-it/end-user-services/laptop-management/laptop-security) for all laptop and desktop systems, there are additional steps required for Linux. The corporate standard is a Dell laptop running **Ubuntu LTS (latest version)** - the only approved Linux distribution. See the [Linux onboarding guide](/handbook/eta/corporate-it/end-user-services/onboarding101/linux-onboarding101/) for detailed installation instructions and required security tools.

## General Applications

- Enable the firewall with the following command:

`$ sudo ufw enable`

- The prompt will respond with "Firewall is active and enabled on system startup".
- Some common applications to install include Google Chrome, Slack, and Zoom. Not all may be available via the normal Ubuntu repository, but you can download them via their respective sites with up-to-date installation instructions:
  - [Google Chrome](https://www.google.com/chrome/)
  - [Slack](https://slack.com/downloads/linux)
  - [Zoom](https://zoom.us/download)
  - Checkout our [Tools page](/handbook/tools-and-tips/) for more potential items.

## Usage of Java

Some applications used on Linux may require Java. The last open-source version of Oracle Java that was released was in January of 2019. All new versions since then require a paid/licensed scubscription. Therefore GitLab no longer supports Oracle Java, and requires all team-members to use an open-source alternative like OpenJDK. Oracle periodicaly audits all downloads of Oracle Java and actively pursues companies that are out of compliance. The IT department therefore enforces a policy that will remove all instances of Oracle Java that are found on team-members machines

To ensure you are using the correct version, use the `java -version` command.

If OpenJDK is installed, the response will look similar to this:

``` shell
$ java -version
openjdk version "11.0.14.1" 2022-02-08
OpenJDK Runtime Environment (build 11.0.14.1+1-Ubuntu-0ubuntu1.20.04)
OpenJDK 64-Bit Server VM (build 11.0.14.1+1-Ubuntu-0ubuntu1.20.04, mixed mode, sharing)
```

If Oracle Java is installed, the response will look similar to this:

``` shell
$ java -version
java version "16.0.1" 2021-04-20
Java(TM) SE Runtime Environment (build 16.0.1+9-24)
Java Hotspot(TM) 64-Bit Server VM (build 16.0.1+9-24, mixed mode, sharing)
```

Most systems will be running either the OpenJDK version or Java will not be installed. If Java is not installed and you wish to install OpenJDK, follow the instructions for installation you received after running the `$ java -version` command. If you are running the Oracle Java version, follow the instructions [here](https://linuxhint.com/uninstall-java-ubuntu/) for Ubuntu.

## Dell and Nvidia

Some GitLab team members have experienced issues with the Nvidia drivers on Dell, including battery drain due to sleep issues when the laptop is closed, random lockups when waking the laptop up, and so on. If this happens, consider the following steps:

- Examine the /etc/default/grub file, the line containing `GRUB_CMDLINE_LINUX_DEFAULT`may look like this:

 `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`

- Edit the line to look like this:

 `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=deep"`

- Then update grub:

 `$ sudo update-grub`

This has reported to work with latest versions of the Nvidia drivers (as of Dec 2019) so you can update the drivers.

## Engineering/coding tools

- It's advised to have some sort of version manager for programming languages as
  what's supplied by repos is typically not sufficient
  - [asdf](https://github.com/asdf-vm/asdf) is pretty good, and usable across
    many platforms
    - This project includes a [large amount of plugins](https://github.com/asdf-vm/asdf-plugins)
      to control various packages as well as languages that you'd need
  - [mise](https://mise.jdx.dev/) is an `asdf`-compatible modern replacement widely used throughout the organization
- Other common packages - this list includes things that always appear to be
  required no matter what realm of work you are in:
  - `gcc`
  - `git`
  - `libssl-dev`
  - `make`
  - `zlib1g-dev`
- Abide by our [security practices](/handbook/security/):

## Production engineering

- If you're a Production Engineer, consider the following:
  - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
  - [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
  - [Docker](https://docs.docker.com/get-started/get-docker/)
  - [Vagrant](https://developer.hashicorp.com/vagrant/install)
  - [VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
  - [gcloud CLI](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)
- Other important packages:
  - `gnupg2`
  - `pwgen`
  - `scdaemon`
  - `yubikey-personalization`
- If you chose to utilize `asdf` as mentioned above, install a few plugins to
  prep yourself to be ready to install a few tools in the future:
  - `asdf plugin-add golang`
  - `asdf plugin-add kubectl`
  - `asdf plugin-add minikube`
  - `asdf plugin-add ruby`
  - `asdf plugin-add terraform`
- Then you'll need to find out which version of the above needs to be installed
  - Check the appropriate repos or ask someone (versions listed are examples):
  - `asdf install ruby 2.4.4`
  - `asdf install terraform 0.11.5`

## Development

- In development, you'll probably need the following packages installed:
  - `cmake`
  - `g++`
  - `krb5`
  - `libkrb5-dev`
  - `libmysqlclient-dev`
  - `libpq-dev`
  - `libre2-dev`
  - `libsqlite3-dev`
- If you chose to utilize `asdf` as mentioned above, install a few plugins to
  prep yourself to be ready to install a few tools in the future:
  - `asdf plugin-add nodejs`
  - `asdf plugin-add postgres`
  - `asdf plugin-add ruby`
- Then you'll need to find out which version of the above needs to be installed
  - Check the appropriate repos or ask someone (versions listed are examples):
  - `asdf install ruby 2.4.4`
  - `asdf install nodejs 8.11.3`

## Enabling the fingerprint reader

Some of the authorized Dell laptops come with a fingerprint reader which is not supported by their official Ubuntu images. However, the fingerprint reader can be enabled using [fprintd](https://fprint.freedesktop.org/).

- Install the required software:

``` shell
sudo apt install fprintd libpam-fprintd
```

- Update the PAM configuration:

``` shell
sudo pam-auth-update
```

- Edit the `/etc/pam.d/common-auth` configuration to enable fingerprint authorization in the terminal and other password prompts. Find the `auth [success=1 default=ignore] pam_unix.so nullok_secure` line and replace it with the following two lines.

``` shell
auth    [success=2 default=ignore]      pam_fprintd.so max-tries=3 timeout=10
auth    [success=1 default=ignore]      pam_unix.so nullok_secure
```

  Note that `max-tries` is the number of fingerprint scans you can attempt until prompted for a password instead, and `timeout` is how long you have to scan your fingerprint before the authorization times out. You can configure these to your requirements.

- Enable fingerprint authorization on the login screen (`sddm`) by editing the `/etc/pam.d/sddm` file and adding the following lines **at the top of the file**.

``` shell
auth        sufficient        pam_unix.so try_first_pass likeauth nullok
auth        sufficient        pam_fprintd.so
```

- Finally, enroll your fingerprint with `fprintd`:

``` shell
fprintd-enroll $USER
```

Fingerprint login and authorization has now been enabled! Note that the sddm login screen has an unintuitive user interface. You'll be prompted with a password field as usual. Press enter and the screen will fade slightly. Now you can scan your fingerprint to log in.

## Troubleshooting

### Zoom screen sharing on GNOME on Wayland

In order to share the user's screen on GNOME on Wayland, Zoom uses a private schreenshot API to chain successive screenshots into a stream. [As GNOME 41, those private D-Bus APIs have been restricted to their intended callers for security reasons, so that hack no longer works.](https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/4665#note_1283742).

As a workaround, you can use [looking glass](https://wiki.gnome.org/Projects/GnomeShell/LookingGlass) to set `global.context.unsafe_mode = true`. You can reinstate default security settings either by ending the session, or by running `global.context.unsafe_mode = true`.

Some caveats apply to this workaround.

- You are disabling a security setting. (This is no worse than a default Xorg session.)
- Zoom freezes for about 15 seconds when initiating a screen sharing session. Wait through the "application not responding" dialogue if it appears, and the "select display" prompt will appear.
- You can share whole desktops, but you cannot share individual application windows.
- Zoom freezes for about 5 seconds upon ending a screen sharing session.
- This workaround must be applied at each login.

### Common issues

Here's a list of common situations that prove to be problematic on Linux.

- You'll want to ensure these components work as desired:
  - Audio through various types of headphones
  - Video capturing - Zoom video and Zoom screen sharing
  - Display - screen resolution or video card related issues
- When having problems with Okta under Linux, make sure to use the latest Chrome (not Chromium) and your Yubi-Key or a phone without a custom ROM
