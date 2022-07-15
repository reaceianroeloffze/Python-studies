from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    full_name = make_full_name('Reace', 'Roeloffze')
    assert isinstance(full_name, str)
    
    assert make_full_name('Reace', 'Roeloffze') == 'Roeloffze; Reace'
    assert make_full_name('Carri-Ann', 'van der Westhuizen') == 'van der Westhuizen; Carri-Ann'
    assert make_full_name('Mzinchileftinstein', 'Raharizoandrinirina') == 'Raharizoandrinirina; Mzinchileftinstein'
    assert make_full_name('Candice', 'DuPlessis-Pretorius') == 'DuPlessis-Pretorius; Candice'
    assert extract_family_name('', '') == '; '
    
def test_extract_family_name():
    family_name = extract_family_name('Roeloffze; Reace')
    assert isinstance(family_name, str)
    
    assert extract_family_name('Roeloffze; Reace') == 'Roeloffze'
    assert extract_family_name('van der Westhuizen; Carri-Ann') == 'van der Westhuizen'
    assert extract_family_name('Raharizoandrinirina; Mzinchileftinstein') == 'Raharizoandrinirina'
    assert extract_family_name('DuPlessis-Pretorius; Candice') == 'DuPlessis-Pretorius'
    assert extract_family_name('; ') == ''
    
def test_extract_given_name():
    given_name = extract_given_name('Roeloffze; Reace')
    assert isinstance(given_name, str)
    
    assert extract_given_name('Roeloffze; Reace') == 'Reace'
    assert extract_given_name('van der Westhuizen; Carri-Ann') == 'Carri-Ann'
    assert extract_given_name('Raharizoandrinirina; Mzinchileftinstein') == 'Mzinchileftinstein'
    assert extract_given_name('DuPlessis-Pretorius; Candice') == 'Candice'
    assert extract_family_name('; ') == ''
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])