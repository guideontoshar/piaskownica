PYSIDEUIC="$(CYBID_PYTHON)\\envs\\humsim\\python.exe" "$(CYBID_PYTHON)\\envs\\humsim\\Library\\bin\\pyside2-uic"
PYSIDERCC="$(CYBID_PYTHON)\\envs\\humsim\\Library\\bin\\pyside2-rcc"

PYSIDEUIC="$(CYBID_PYTHON)\\python.exe" "$(CYBID_PYTHON)\\Scripts\\pyside2-uic.exe"
PYSIDERCC="$(CYBID_PYTHON)\\Scripts\\pyside2-rcc.exe"
QT5UIC="$(CYBID_PYTHON)\\Scripts\\pyuic5.exe"
QT5RCC="$(CYBID_PYTHON)\\Scripts\\pyrcc5.exe"

ifdef QT_API
    ifeq "$(QT_API)" "pyside2"
        UICTOOL=$(PYSIDEUIC)
        RCCTOOL=$(PYSIDERCC)
    else
        UICTOOL=$(QT5UIC)
        RCCTOOL=$(QT5RCC)
    endif
else
    UICTOOL=$(QT5UIC)
    RCCTOOL=$(QT5RCC)
endif

all: 
	@echo "Targets are: testall(aka: alltest) allexamples"

alltest: testall

alltests: testall

testall:
	@echo "Run all tests"
	$(PYTHON) -m unittest discover

allexamples:
	cd examples && make allexamples

updategui: mainwindow.ui
	$(PYSIDEUIC) $< -o ui_mainwindow.py

clean : 
	rm -f ui_mainwindow.py
	rm -rf __pycache__
