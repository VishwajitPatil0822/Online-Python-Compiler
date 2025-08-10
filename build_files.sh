# build_files.sh

# Collect Django static files
python3 manage.py collectstatic --noinput

# Create the directory for static files build
mkdir -p staticfiles_build

# Copy all collected static files into the build directory
cp -r staticfiles/* staticfiles_build/
