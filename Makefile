make: clean
	python -O -m py_compile __init__.py
	mkdir ./bin
	mv __init__.pyo ./bin/libnotify-terminal

clean:
	rm -rf ./bin

install:
	chmod 755 ./bin/libnotify-terminal
	cp ./bin/libnotify-terminal /usr/bin/

uninstall:
	rm /usr/bin/libnotify-terminal