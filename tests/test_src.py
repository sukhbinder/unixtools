# Save this in a file named test_text_tools.py

from unixtools import cut_text, wc, extract_text_from_file

def test_cut_text():
    text = "apple,banana,orange\n1,2,3\nx,y,z"
    expected_output = "apple\n1\nx\n"

    assert cut_text(text, ',', [1]) == expected_output

def test_wc():
    text = "Hello, how are you?\nI am doing well, thank you."
    expected_lines = 2
    expected_words = 10
    expected_chars = 45

    lines, words, characters = wc(text)
    assert lines == expected_lines
    assert words == expected_words
    assert characters == expected_chars

def test_extract_text_from_file(tmp_path):
    # Create a temporary test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

    # Test extracting lines 2 to 4 from the temporary test file
    expected_output = "Line 2\nLine 3\nLine 4\n"
    assert extract_text_from_file(str(test_file), 2, 4) == expected_output
