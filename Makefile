INSTALL_DIR	= /usr/bin

make: clean
	python -O -m py_compile src/libnotify-terminal.py
	mv src/libnotify-terminal.pyo ./bin/libnotify-terminal
	chmod 755 ./bin/libnotify-terminal

clean:
	rm -rf ./bin
	rm -rf ./**/*.py[cod]
	mkdir bin

install:
	mkdir -p $(INSTALL_DIR)
	chmod 755 ./bin/libnotify-terminal
	cp ./bin/* $(INSTALL_DIR)

uninstall:
	rm /usr/bin/libnotify-terminal

test-compile:
	./bin/libnotify-terminal --title "New Message" \
		--subtitle "Ali Connors" --body "Hey, you down for dinner?" \
		--reply --reply-to "Ali Connors" \
		--reply-message "Hey, you down for dinner?"

test:
	libnotify-terminal --title "New Message" \
		--subtitle "Ali Connors" --body "Hey, you down for dinner?" \
		--reply --reply-to "Ali Connors" \
		--reply-message "Hey, you down for dinner?"