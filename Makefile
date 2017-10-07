INSTALL_DIR	= /usr/bin

make: clean libnotify-terminal

libnotify-terminal: src/libnotify_terminal.py
	./scripts/build.py
	chmod +x libnotify-terminal

clean:
	rm -f libnotify-terminal .coverage coverage.xml

install: make
	python setup.py install
	mkdir -p $(INSTALL_DIR)
	chmod 755 ./bin/libnotify-terminal
	cp ./bin/* $(INSTALL_DIR)

uninstall:
	rm /usr/bin/libnotify-terminal

test-compile:
	./libnotify-terminal --title "New Message" \
		--subtitle "Ali Connors" --body "Hey, you down for dinner?" \
		--reply --reply-to "Ali Connors" \
		--reply-message "Hey, you down for dinner?"

test:
	python -m pytest tests/test_libnotify.py

coverage:
	coverage run -m pytest tests/test_libnotify.py
	coverage xml
	python-codacy-coverage -r coverage.xml
	rm coverage.xml