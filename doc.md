| /do/buttons/check   |                                                |
|:--------------------|:-----------------------------------------------|
| Info                | [beta] [gpio] [buttons] [electronics] [python] |
| Description         | Use this to check if buttons service works     |
| Usage               | /do/buttons/check                              |
| Modules             | exec python -u /do/buttons/python/buttons.py,  |

| /do/buttons/commands   |                                                               |
|:-----------------------|:--------------------------------------------------------------|
| Info                   | [beta] [gpio] [buttons] [electronics] [cat]                   |
| Description            | Show buttons configuration (/user/config/buttons/buttons.cfg) |
| Usage                  | /do/buttons/commands                                          |

| /do/buttons/install             |                                                                                                 |
|:--------------------------------|:------------------------------------------------------------------------------------------------|
| Info                            | [beta] [gpio] [buttons] [electronics] [supervisor] [wiringPi]                                   |
| Description                     | Install buttons module                                                                          |
| Usage                           | /do/buttons/install                                                                             |
| Softwares                       | supervisor, WiringPi,                                                                           |
| Modules                         | command=/do/buttons/check, cp -v /do/buttons/conf/buttons.cfg /user/config/buttons/buttons.cfg, |
| System                          | /system/install supervisor, /system/makedir /user/config/buttons, /system/installWiringPi,      |
| 1. Install buttons as a service |                                                                                                 |
| 2. Copy config files            |                                                                                                 |

| /do/buttons/log   |                                                    |
|:------------------|:---------------------------------------------------|
| Info              | [beta] [gpio] [buttons] [electronics] [log] [tail] |
| Description       | Show service status and display and of log         |
| Usage             | /do/buttons/log                                    |
| 1. buttons Status |                                                    |
| 1. Status         |                                                    |
| 2. Log            |                                                    |

| /do/buttons/press    |                                       |
|:---------------------|:--------------------------------------|
| Info                 | [beta] [gpio] [buttons] [electronics] |
| Description          | Simulate a button with gpio utility   |
| Usage                | /do/buttons/press bcmPin              |
| Example              | /do/buttons/press 26                  |
| Variables            | pin=$(/system/bcmToWpi $1),           |
| System               | pin=$(/system/bcmToWpi $1),           |
| 1. Simulate Press $1 |                                       |

| /do/buttons/restart   |                                                    |
|:----------------------|:---------------------------------------------------|
| Info                  | [beta] [gpio] [buttons] [electronics] [supervisor] |
| Description           | Restart buttons service                            |
| Usage                 | /do/buttons/restart                                |
| Modules               | /do/buttons/stop, /do/buttons/start,               |
| 1. [BUTTONS] Restart  |                                                    |

| /do/buttons/settings   |                                                            |
|:-----------------------|:-----------------------------------------------------------|
| Info                   | [beta] [gpio] [buttons] [electronics] [interactive] [nano] |
| Description            | Modify buttons configuration, restart it and show log      |
| Usage                  | /do/buttons/settings                                       |
| Modules                | /do/buttons/restart, /do/buttons/log,                      |

| /do/buttons/start   |                                                    |
|:--------------------|:---------------------------------------------------|
| Info                | [beta] [gpio] [buttons] [electronics] [supervisor] |
| Description         | Start buttons service                              |
| Usage               | /do/buttons/start                                  |
| 1. [BUTTONS] start  |                                                    |

| /do/buttons/state   |                                                          |
|:--------------------|:---------------------------------------------------------|
| Info                | [beta] [gpio] [buttons] [electronics] [supervisor] [bcm] |
| Description         | Show state of button (bcm) using gpio utility            |
| Usage               | /do/buttons/state bcmPin                                 |
| Example             | /do/buttons/state 26                                     |
| Variables           | state=$(gpio read $(/system/bcmToWpi $1)),               |
| System              | state=$(gpio read $(/system/bcmToWpi $1)),               |

| /do/buttons/stop   |                                                    |
|:-------------------|:---------------------------------------------------|
| Info               | [beta] [gpio] [buttons] [electronics] [supervisor] |
| Description        | Stop buttons service                               |
| Usage              | /do/buttons/stop                                   |
| 1. [BUTTONS] stop  |                                                    |

| /do/buttons/uninstall   |                                                         |
|:------------------------|:--------------------------------------------------------|
| Info                    | [beta] [gpio] [buttons] [electronics] [supervisor]      |
| Description             | Uninstall buttons service                               |
| Usage                   | /do/buttons/uninstall                                   |
| System                  | /system/autoBackup /etc/supervisor/conf.d/buttons.conf, |
| 1. [BUTTONS] Remove     |                                                         |

