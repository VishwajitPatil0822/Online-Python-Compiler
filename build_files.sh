# build_files.sh

# Create the directory where collected static files will be stored
mkdir -p staticfiles_build

# Copy existing static files into the build directory
cp -r static/* staticfiles_build/ || true
