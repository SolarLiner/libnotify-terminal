INSTALL_DIR	= /usr/bin

make: clean coverage
	python -O -m py_compile src/libnotify_terminal.py
	mv src/libnotify_terminal.pyo ./libnotify-terminal
	chmod 755 ./libnotify-terminal

clean:
	rm -rf ./bin
	rm -rf ./**/*.py[cod]
	mkdir bin

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