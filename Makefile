INSTALL_DIR	= /usr/bin

make: clean
	python -O -m py_compile libnotify-terminal.py
	mv libnotify-terminal.pyo ./bin/libnotify-terminal
	chmod 755 ./bin/libnotifier-terminal

clean:
	rm -rf ./bin
	mkdir bin

install:
	mkdir -p $(INSTALL_DIR)
	chmod 755 ./bin/libnotify-terminal
	cp ./bin/* $(INSTALL_DIR)

uninstall:
	rm /usr/bin/libnotify-terminal

test:
	./bin/libnotify-terminal --title "New Message" \
		--subtitle "Ali Connors" --body "Hey, you down for dinner?" \
		--reply --reply-to "Ali Connors" \
		--reply-message "Hey, you down for dinner?"