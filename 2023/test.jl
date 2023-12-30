function create_function(MyType, value)
	v = value+1
	function test(a::MyType, b::MyType) where MyType
		return a+b+v
	end
	return test
end

test = create_function(Int, 10)


display(test(10, 20))
