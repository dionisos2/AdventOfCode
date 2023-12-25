module Day17

export parse_input, day17, day17_2

using InteractiveUtils
using OrderedCollections
using Compat
using DataStructures

struct Node
	coords::Tuple{Int, Int}
	last_move::Tuple{Int, Int}
	move::Int
end

function parse_input(file_path)
	open(file_path) do file
		return permutedims(stack(eachline(file)))
	end
end

function create_a_star_functions(city)
  function heuristic(node)
    gi, gj = size(city)
    bi, bj = node.coords
    return (gi - bi) + (gj - bj)
  end

  function cost(_, node2)
		return parse(Int, city[node2.coords...])
  end

	in_boundaries(matrix, coords) = all((1,1) .<= coords .<= size(matrix))
  function get_neighbours(node::Node)
		dirs = ((0,1), (0,-1), (1,0), (-1,0))
		result = []

		for dir in dirs
			new_coords = node.coords.+dir
			if in_boundaries(city, new_coords)
				if node.last_move == dir && node.move < 3
					new_node = Node(new_coords, node.last_move, node.move+1)
					push!(result, new_node)
				elseif node.last_move != dir
					new_node = Node(new_coords, dir, 1)
					push!(result, new_node)
				end
			end
		end

		return result
  end

  function isgoal(node)
    return node.coords == size(city)
  end




	return (get_neighbours=get_neighbours, isgoal=isgoal, cost=cost, heuristic=heuristic)
end

function reconstruct_path(come_from, current)
  total_path = [current]
  while current in keys(come_from)
    current = come_from[current]
    pushfirst!(total_path, current)
  end
  return total_path
end

function a_star(start, get_neighbours, isgoal, cost, heuristic)
	come_from = Dict()
	gscore = DefaultDict(Inf)
	gscore[start] = 0
	fscore = DefaultDict(Inf)
	fscore[start] = heuristic(start)


	isless(node1::Node, node2::Node) = fscore[node1] < fscore[node2]

	heap_nodes = MutableBinaryHeap(Base.Order.Lt(isless), [start])
	nodes = Set([start])

	while !isempty(heap_nodes)
		current = pop!(heap_nodes)
		delete!(nodes, current)
		if isgoal(current)
			return reconstruct_path(come_from, current)
		end

		for neighbour in get_neighbours(current)
			score = gscore[current] + cost(current, neighbour)
			if score < gscore[neighbour]
				come_from[neighbour] = current
				gscore[neighbour] = score
				fscore[neighbour] = score + heuristic(neighbour)
				push!(heap_nodes, neighbour)
				push!(nodes, neighbour)
			end
		end
	end
	return nothing
end

function display_path(city, path)
	for (i, line) in enumerate(eachrow(city))
		println()
		for (j, char) in enumerate(line)
			found = findall(node->node.coords == (i, j), path)
			if isempty(found)
				print(char)
			else
				print('#')
			end
		end
	end
end

function day17(city)
	funcs = create_a_star_functions(city)
	start = Node((1, 1), (0, 0), 0)
	path = a_star(start, funcs...)
	println(path)
	cost = funcs[:cost]
	display_path(city, path)
	println()
	return sum(cost(nothing,node) for node in path)
end

function day17_2(city)
	return city
end

city = parse_input("input17_test")
result = day17(city)

display(result)
clipboard(string(result))

end
