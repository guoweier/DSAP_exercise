# There seems to be some redundacy in the repertoire of the positional list ADT, as the operation L.add_first(e) could be enacted by the alternative L.add_before(L.first(), e). Likewise, L.add_last(e) might be performed as L.add_after(L.last(), e). Explain why the methods add_first and add_last are necessary.

# Because if L is empty, then L.first() returns None.
# Then in add_before(), it will return an Error message that the input element is not valid.
# So finally it will fails to add first Node in the Positional List.
# Same thing for add_last. 
