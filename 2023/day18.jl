module Day18

export parse_input, day18, day18_2

using InteractiveUtils
using OrderedCollections
using Compat

function parse_input(file_path)
	open(file_path) do file
		result = []

		dir_code=Dict("R"=>(0, 1), "L"=>(0, -1), "D"=>(1, 0), "U"=>(-1, 0))

    for line in eachline(file)
			dir, value, color = split(line)
			dir = dir_code[dir]
			value = parse(Int, value)
			push!(result, (dir=dir, value=value, color=color))
    end

		return result
  end
end


function day18(dig_plan)
	return dig_plan
end

function day18_2(dig_plan)
	return dig_plan
end

dig_plan = parse_input("input18_test")
result = day18(dig_plan)

display(result)
clipboard(string(result))

end
