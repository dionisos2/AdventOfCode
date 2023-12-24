module Day15

export parse_input, day15

using InteractiveUtils
using OrderedCollections

function parse_input(file_path)
	open(file_path) do file
		line = readline(file)
		result = split(line, ",")
		return result
  end
end

function get_hash(str)
	current_value = 0
	for char in str
		current_value += Int(char)
		current_value = (current_value * 17)%256
	end
	return current_value
end

function day15(data)
	return sum(get_hash.(data))
end

const re_add = r"(\w*)=(\d*)"
const re_remove = r"(\w*)-"

function get_op(str)
	add = match(re_add, str)
	if add !== nothing
		return add[1], add[2]
	end

	remove = match(re_remove, str)
	if remove !== nothing
		return remove[1], nothing
	end

end

function day15_2(data)
	boxes = [OrderedDict() for _ in 1:256]

	for step in data
		label, focal = get_op(step)
		box = boxes[get_hash(label)+1]
		if focal === nothing
			delete!(box, label)
		else
			box[label] = parse(Int, focal)
		end
	end

	result = 0
	for (index, box) in enumerate(boxes)
		for (slot, op) in enumerate(box)
			result += index * slot * op[2]
		end
	end

	return result
end

data = parse_input("input15")
result = day15_2(data)

println(result)
clipboard(string(result))

end
