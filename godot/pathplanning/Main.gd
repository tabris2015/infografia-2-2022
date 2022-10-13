extends Node2D

func _unhandled_input(event):
	if event is InputEventMouseButton:
		# verificar que el evento sea clic izq
		if event.button_index == BUTTON_LEFT and event.pressed:
			# PoolVector2Array
			var path = $Navigation2D.get_simple_path(
				$Player.global_position, 
				event.global_position
				)
			print(path)
			$Line2D.points = path
			$Player.path = path
