extends RigidBody2D


func _on_playerf_body_entered(body):
	print("ouch " + body.get_name())
