extends Node2D


onready var _animation_player = $AnimationPlayer

func _process(delta):
	if Input.is_action_pressed("ui_up"):
		_animation_player.play("idle")
	else:
		_animation_player.stop()
