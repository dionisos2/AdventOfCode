module Day16

export parse_input, day16, day16_2

using InteractiveUtils
using OrderedCollections

function parse_input(file_path)
	open(file_path) do file
		result = []

    for line in eachline(file)
			push!(result, line)
    end

		return result
  end
end


function day16(data)
	return data
end

function day16_2(data)
	return data
end

data = parse_input("input16_test")
result = day16(data)

println(result)
clipboard(string(result))

end
