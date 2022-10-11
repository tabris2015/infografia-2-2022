extends KinematicBody2D

export(int) var w_range = 50

var speed = 200
var accel = 2
var velocity = Vector2.ZERO
onready var state_machine = $AnimationTree.get("parameters/playback")

onready var start_position = global_position
onready var target_position = global_position

onready var timer = $Timer

func update_target_position():
	var target_vector = Vector2(rand_range(-w_range, w_range), rand_range(-w_range, w_range))
	print(target_vector)
	target_position = start_position + target_vector
	state_machine.travel("walk")

func _physics_process(delta):
	var direction = global_position.direction_to(target_position)
	if direction.x < 0:
		$Sprite.scale.x = -1
	else:
		$Sprite.scale.x = 1
	velocity = velocity.move_toward(direction * speed, accel * delta)
	if global_position.distance_to(target_position) < 0.1:
		state_machine.travel("idle")
		velocity = Vector2.ZERO
	move_and_slide(velocity)

func _on_Timer_timeout():
	print("mover")
	update_target_position()
	var duration = rand_range(10, 16)
	timer.start(duration)

