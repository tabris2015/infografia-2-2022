extends RigidBody2D



func _on_character2_body_entered(body):
	print("colision con: " + body.get_name())
