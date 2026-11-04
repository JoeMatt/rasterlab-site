PORT ?= 8080
STRICT ?= 0

.PHONY: serve check help
help:
	@echo "make serve   # static server on http://localhost:$(PORT)/"
	@echo "make check   # validate links, anchors, assets (STRICT=1 fails on draft markers)"
serve:
	python3 -m http.server $(PORT) --bind 127.0.0.1
check:
	python3 -I scripts/check.py $(if $(filter 1,$(STRICT)),--strict,)
