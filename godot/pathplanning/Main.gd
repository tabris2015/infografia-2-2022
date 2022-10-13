extends Node2D

func _unhandled_input(event):
	if event is InputEventMouseButton:
		# verificar que el evento sea clic izq
		if event.button_index == BUTTON_LEFT and event.pressed:
			# PoolVector2Array
			var path_player = $Navigation2D.get_simple_path(
				$Player.global_position, 
				event.global_position
				)
			
			print(path_player)
			$Line2D.points = path_player
			$Player.path = path_player

func _process(delta):
	var path_pet = $Navigation2D.get_simple_path(
				$Pet.global_position,
				$Player.global_position
			)
			
	$LinePet.points = path_pet
	$Pet.path = path_pet
	
