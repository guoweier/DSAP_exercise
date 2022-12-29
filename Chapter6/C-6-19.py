# In Code Fragment 6.5 we assume that opening tags in HTML have form <name>, as with <li>. More generally, HTML allows optional attributes to be expressed as part of an opening tag. The general form used is <name attribute1="value1" atturbute2="value2">; for example, a table can be given a border and additional padding by using an opening tag of <table border="3" cellpadding="5">. Modify Code Fragment 6.5 so that it can properly match tags, even when an opening tag may include one or more such attributes.

# Example:
# <name attribute1="value1" atturbute2="value2"> This is baibey. </name>

def is_matched_html(raw):
    """Return True if all HTML tags are properly match. False otherwise."""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith("/"):
            S.push(tag)
        else:                                   # if it is the close tag 
            if S.is_empty():
                return False
            if not S.pop().startswith(tag[1:]): # the close tag name should match the open tag name
                return False
        j = raw.find('<', k+1)
    return S.is_empty()
