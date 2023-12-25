module Day16

export parse_input, day16, day16_2

using InteractiveUtils
using OrderedCollections
using Compat
using Profile
using StatProfilerHTML

function parse_input(file_path)
	open(file_path) do file
		return permutedims(stack(eachline(file)))
	end
end


in_boundaries(contraption, pos) = all((1,1) .<= pos .<= size(contraption))

function next_step(contraption, light_matrix, light)
	pos, dir = light
	light_pos = pos.+dir

	if in_boundaries(contraption, pos)
		if dir ∉ light_matrix[pos...]
			push!(light_matrix[pos...], dir)
		else
			return []
		end
	end

	if in_boundaries(contraption, light_pos)
		char = contraption[light_pos...]
		di, dj = dir # ↓,→
		if (char == '.') || (char == '-' && dj != 0) || (char == '|' && di != 0)
			return [(light_pos, dir)]
		elseif char == '\\'
			return [(light_pos, (dj, di))]
		elseif char == '/'
			return [(light_pos, (dj*(-1), di*(-1)))]
		elseif char == '-' && di != 0
			return [(light_pos, (0, 1)) , (light_pos, (0, -1))]
		elseif char == '|' && dj != 0
			return [(light_pos, (1, 0)) , (light_pos, (-1, 0))]
		else
			return []
		end

	end

	return []
end

function next_steps(contraption, light_matrix, lights)
	result = []

	for light in lights
		steps = next_step(contraption, light_matrix, light)
		append!(result, steps)
	end

	return result
end

function show(contraption, lights)
	for (i, line) in enumerate(eachrow(contraption))
		println()
		for (j, char) in enumerate(line)
			found = findall(x->x[1]==(i,j), lights)
			if isempty(found)
				print(char)
			else
				print("#")
			end
		end
	end
end

function day16(contraption, light = ((1,0), (0,1)))
	msize = size(contraption)
	light_matrix = [Set() for _ in 1:msize[1], _ in 1:msize[2]]

	current_lights = [light]

	while !isempty(current_lights)
		current_lights = next_steps(contraption, light_matrix, current_lights)
	end

	return sum(!isempty(lights) for lights in light_matrix)
end

function day16_2(contraption)
	max_energy = 0
	li, lj = size(contraption)

	for i in 1:li
		light = ((i, 0), (0, 1))
		max_energy = max(max_energy, day16(contraption, light))
		light = ((i, lj+1), (0, -1))
		max_energy = max(max_energy, day16(contraption, light))
	end

	for j in 1:lj
		light = ((0, j), (1, 0))
		max_energy = max(max_energy, day16(contraption, light))
		light = ((lj+1, j), (-1, 0))
		max_energy = max(max_energy, day16(contraption, light))
	end

	return max_energy
end

contraption = parse_input("input16")
result = day16_2(contraption)

display(result)
clipboard(string(result))

end
