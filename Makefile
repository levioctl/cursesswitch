install:
	sudo pip install -U -r requirements.txt
	sudo python setup.py install

check_convention:
	pep8 cursesswitch

clean:
	rm -rf AUTHORS build ChangeLog *.egg-info
