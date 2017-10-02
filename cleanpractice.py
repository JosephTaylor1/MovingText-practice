from sys import argv

script, arg1, arg2 = argv

test = open(arg1, 'a')

print "Ok let's write some text in %r." % arg1
added_text = raw_input('>')

test.write(added_text)

updated_test = open(arg1)
up_test = updated_test.read()

print "Now that you decided to add %r, into your %r file.  We are gonna actually write it in." % (added_text, arg2)

test2 = open(arg2)
test2.write(up_test, 'a')

print  "If that worked we should be able to get all the new text in %r." % arg2

test.close()
test2.close()
