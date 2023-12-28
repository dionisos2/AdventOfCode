module Day17

export parse_input, day17, day17_2

using InteractiveUtils
using OrderedCollections
using Compat
using DataStructures
using BenchmarkTools
using StatProfilerHTML

struct Node
	coords::Tuple{Int, Int}
	last_move::Tuple{Int, Int}
	move::Int
end

function parse_input(file_path)
	open(file_path) do file
		return map(x->parse(Int, x), permutedims(stack(eachline(file))))
	end
end

in_boundaries(matrix, coords) = all((1,1) .<= coords .<= size(matrix))

function create_a_star_functions(city)
  function heuristic(node::Node)
    gi, gj = size(city)
    bi, bj = node.coords
    return (gi - bi) + (gj - bj)
  end

	min_cost = fill(0, size(city))
	li, lj = size(city)

	for (i, line) in Iterators.reverse(enumerate(eachrow(city)))
		for (j, value) in Iterators.reverse(enumerate(line))
			if i+1 > li && j+1 > lj
				min_cost[i, j] = value
			elseif i+1 > li
				min_cost[i, j] = value + min_cost[i, j+1]
			elseif j+1 > lj
				min_cost[i, j] = value + min_cost[i+1, j]
			else
				min_cost[i, j] = value + min(min_cost[i, j+1], min_cost[i+1, j])
			end
		end
	end

	function better_heuristic(node::Node)::Int
		return min_cost[node.coords...]
	end

  function cost(_, node2::Node)::Int
		return city[node2.coords...]
  end

  function get_neighbours(node::Node)::Array{Node}
		i, j = node.last_move
		dirs = ((i, j), (j, i), (-j, -i))
		result = Node[]

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

  function isgoal(node::Node)
    return node.coords == size(city)
  end

	return (get_neighbours=get_neighbours, isgoal=isgoal, cost=cost, heuristic=better_heuristic)
end

function reconstruct_path(come_from, current::Node)
  total_path = [current]
  while current in keys(come_from)
    current = come_from[current]
    pushfirst!(total_path, current)
  end
  return total_path
end

const NodeType=Node
function a_star(start, get_neighbours, isgoal, cost, heuristic)
	come_from = Dict{NodeType, NodeType}()
	gscore = DefaultDict{NodeType, Int}(typemax(Int))
	gscore[start] = 0
	fscore = DefaultDict{NodeType, Int}(typemax(Int))
	fscore[start] = heuristic(start)


	isless(node1::NodeType, node2::NodeType) = fscore[node1] < fscore[node2]

	heap_nodes = MutableBinaryHeap{NodeType}(Base.Order.Lt(isless), [start])
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

function find_length(funcs)
	start = Node((1, 1), (0, 1), 0)
	path = a_star(start, funcs...)
	cost = funcs[:cost]

	return sum(cost(nothing,node) for node in path[2:end])
end

function create_a_star_functions_2(city)
	_, _, cost, heuristic = create_a_star_functions(city)

	function get_neighbours(node::Node)::Array{Node}
		i, j = node.last_move
		dirs = ((i, j), (j, i), (-j, -i))
		result = Node[]

		for dir in dirs
			new_coords = node.coords.+dir
			if in_boundaries(city, new_coords)
				if node.last_move == dir && node.move < 10
					new_node = Node(new_coords, node.last_move, node.move+1)
					push!(result, new_node)
				elseif node.last_move != dir && node.move > 3
					new_node = Node(new_coords, dir, 1)
					push!(result, new_node)
				end
			end
		end
		return result
	end

	function isgoal(node::Node)::Bool
    return node.coords == size(city) && node.move >= 4
  end

	return (get_neighbours=get_neighbours, isgoal=isgoal, cost=cost, heuristic=heuristic)
end

function day17(city)
	return find_length(create_a_star_functions(city))
end

function day17_2(city)
	return find_length(create_a_star_functions_2(city))
end

function compile()
	city = parse_input("input17_test")
	result = day17(city)
	result2 = day17_2(city)
	return (result, result2)
end

display(compile())

city = parse_input("input17")

@btime day17(city)
@btime day17_2(city)
# heuristic :
# 1.195 s (7142074 allocations: 275.69 MiB)
# 6.514 s (26264199 allocations: 1010.81 MiB)
# better_heuristic :
# 613.975 ms (2883789 allocations: 115.30 MiB)
# 3.979 s (14287796 allocations: 544.28 MiB)
# remove principals type instabilities :
# 263.579 ms (180765 allocations: 102.14 MiB)
# 1.357 s (807683 allocations: 509.05 MiB)

# @profilehtml day17_2(city)

result = day17_2(city)
display(result)
clipboard(string(result))

end
