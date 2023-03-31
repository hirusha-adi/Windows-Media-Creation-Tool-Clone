import pages
import runner


if __name__ == "__main__":
    # start the GUI in a new thread
    runner.runThreaded(pages.startGUI)

    # run the modules
    runner.runModules()
