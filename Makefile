
PROGRAM = main.py

upload:
	git add *
	git add Makefile
	git commit -m "MakeUpdate" 
	git branch -M main
	git push -u origin main
	
compile:
	python main.py

start:
	python -m nuitka --follow-imports $(PROGRAM).py
	$(PROGRAM).exe
	
clean:
	rm *.cmd *.exe
