INSTALL_DIR	= /usr/bin/libnotify-terminal

make: clean
	python -O -m py_compile libnotify-terminal.py
	mv libnotify-terminal.pyo ./bin/libnotify-terminal
	mv ./src/*.pyo ./bin

clean:
	rm -rf ./bin
	mkdir bin

install:
	mkdir -p $(INSTALL_DIR)
	chmod 755 ./bin/libnotify-terminal
	cp ./bin/* $(INSTALL_DIR)

uninstall:
	rm /usr/bin/libnotify-terminal