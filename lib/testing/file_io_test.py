from file_io import write_file, append_file, read_file

def test_write_file(tmp_path):
    """Test write_file()"""
    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content

def test_append_file(tmp_path):
    """Test append_file()"""

    file_name = tmp_path / "test_file"
    file_content = "This is a test content.\n"
    append_content = "Appended content."
    write_file(file_name, file_content)
    append_file(file_name, append_content)
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()

    normalized_expected = (file_content + '\n' + append_content).replace('\r\n', '\n')
    normalized_read = file_content_read.replace('\r\n', '\n')

    assert normalized_read == normalized_expected



def test_read_file(tmp_path):
    """Test read_file()"""

    file_name = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_name, file_content)
    file_content_read = read_file(file_name)
    assert file_content_read == file_content
