import time
import pynotify
import sys
import signal
import curses

TIME = 60 * 25
start = time.time()


def notify(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return


def exit_gracefully(signum, frame):
    curses.endwin()
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, exit_gracefully)

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    while True:
        elapsed = time.time() - start
        if elapsed > TIME:
            notify('Pomotodo', 'Time is up!')
            break

        remaining = TIME - elapsed
        m = remaining / 60
        s = remaining % 60

        stdscr.addstr(0, 0, "%02d:%02d" % (m, s))
        stdscr.refresh()

        time.sleep(1)

    exit_gracefully()

if __name__ == '__main__':
    main()
