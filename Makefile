help:
	@echo "bright - Brightness control utility for Linux"
	@echo "Installation options:"
	@echo "    make install - To install the package"
	@echo "    make help    - To display this help message"
	@echo ""
	@echo "Developer Md. Almas Ali"

install:
	# @echo "Installing bright..."
	# @sudo apt-get install -y gcc make libxrandr-dev
	# @echo "Installing bright to /usr/bin"
	# @sudo cp bright /usr/bin
	# @echo "bright installed successfully"

build:
	@echo "Building bright..."
	@gcc bright.c -o bright
	@echo "bright built successfully"