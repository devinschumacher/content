# Glossary

daemons - services that are installed by the user, which usually include all server services. Such services run in the background without any user interaction. identified by the letter '`d`' at the end of the program name, for example, `sshd` or `systemd`.

systemd - This daemon is an `Init process` started first and thus has the process ID (PID) 1. This daemon monitors and takes care of the orderly starting and stopping of other services.

`bash prompt`

`parent process ID (PPID)`  -

`Systemctl` -

Bootloader -

OS Kernel -

---

`shell` -  A Linux terminal, also called a `shell` or command line, provides a text-based input/output (I/O) interface between users and the kernel for a computer system. The term console is also typical but does not refer to a window but a screen in text mode. In the terminal window, commands can be executed to control the system.

We can think of a shell as a text-based GUI in which we enter commands to perform actions like navigating to other directories, working with files, and obtaining information from the system but with way more capabilities.

The most commonly used shell in Linux is the `Bourne-Again Shell` (`BASH`), and is part of the GNU project. Everything we do through the GUI we can do with the shell.

The shell gives us many more possibilities to interact with programs and processes to get information faster. Besides, many processes can be easily automated with smaller or larger scripts that make manual work much easier.  Besides Bash, there also exist other shells like [Tcsh/Csh](https://en.wikipedia.org/wiki/Tcsh), [Ksh](https://en.wikipedia.org/wiki/KornShell), [Zsh](https://en.wikipedia.org/wiki/Z_shell), [Fish](https://en.wikipedia.org/wiki/Friendly_interactive_shell) shell and others.

---

`Terminal Emulators` - Terminal emulation is software that emulates the function of a terminal. It allows the use of text-based programs within a graphical user interface (`GUI`). There are also so-called command-line interfaces (`CLI`) that run as additional terminals in one terminal. In short, a terminal serves as an interface to the shell interpreter.

---

`multiplexer` -  In Linux, a multiplexer (often abbreviated as "mux") refers to a software tool that allows multiple virtual terminals or sessions to share a single physical terminal or console. It enables users to switch between different terminal sessions without the need to open new windows or log in multiple times.

The most commonly used multiplexer in Linux is called "tmux" (short for terminal multiplexer). It is a command-line tool that can be used to manage multiple terminal sessions, windows, and panes within a single terminal window. With tmux, users can split their terminal window into multiple panes, each running its own command or program.

Tmux provides many useful features such as session management, pane and window manipulation, and detachable sessions. It also allows users to customize the appearance and behavior of their terminal environment.

Multiplexers like tmux are especially useful for system administrators and developers who need to manage multiple terminal sessions simultaneously. By using a multiplexer, they can avoid the overhead of opening multiple terminal windows or SSH sessions to remote servers.

---

Utilities -

Window Manager -

| Bootloader      | A piece of code that runs to guide the booting process to start the operating system. Parrot Linux uses the GRUB Bootloader.                                                                                                                                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OS Kernel       | The kernel is the main component of an operating system. It manages the resources for system's I/O devices at the hardware level.                                                                                                                                                                                                               |
| Daemons         | Background services are called "daemons" in Linux. Their purpose is to ensure that key functions such as scheduling, printing, and multimedia are working correctly. These small programs load after we booted or log into the computer.                                                                                                        |
| OS Shell        | The operating system shell or the command language interpreter (also known as the command line) is the interface between the OS and the user. This interface allows the user to tell the OS what to do. The most commonly used shells are Bash, Tcsh/Csh, Ksh, Zsh, and Fish.                                                                   |
| Graphics server | This provides a graphical sub-system (server) called "X" or "X-server" that allows graphical programs to run locally or remotely on the X-windowing system.                                                                                                                                                                                     |
| Window Manager  | Also known as a graphical user interface (GUI). There are many options, including GNOME, KDE, MATE, Unity, and Cinnamon. A desktop environment usually has several applications, including file and web browsers. These allow the user to access and manage the essential and frequently accessed features and services of an operating system. |
| Utilities       | Applications or utilities are programs that perform particular functions for the user or another program.                                                                                                                                                                                                                                       |

linux command line -

