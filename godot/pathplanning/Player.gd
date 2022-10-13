extends Sprite

export var speed = 80
var path = PoolVector2Array()

func _process(delta):
	# calcular la distancia
	var distance_to_move = speed * delta
	
	while distance_to_move > 0 and path.size() > 0:
		var distance_to_next = position.distance_to(path[0])
		if distance_to_move <= distance_to_next:
			position += position.direction_to(path[0]) * distance_to_move
		else:
			position = path[0]
			path.remove(0)
		distance_to_move -= distance_to_next
		
		
