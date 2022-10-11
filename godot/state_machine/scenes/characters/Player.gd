extends KinematicBody2D

const ACCEL = 500
const MAX_SPEED = 80
const FRICTION = 500

var hp = 5
var velocity = Vector2.ZERO
onready var state_machine = $AnimationTree.get("parameters/playback")
var hurt = false
var die = false

func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	input_vector = input_vector.normalized()
	
	if input_vector != Vector2.ZERO:
		velocity = velocity.move_toward(input_vector * MAX_SPEED, ACCEL * delta)
		state_machine.travel("run")
	else:
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
		state_machine.travel("idle")
		
	if Input.is_action_just_pressed("attack"):
		state_machine.travel("attack1")
	if Input.is_action_just_pressed("power_attack"):
		state_machine.travel("attack3")
	if Input.is_action_just_pressed("roll"):
		state_machine.travel("roll")
	
	if Input.is_action_pressed("block"):
		state_machine.travel("block_idle")
		velocity = Vector2.ZERO
	
	if hurt:
		state_machine.travel("hurt")
		hurt = false
	
	if die:
		state_machine.travel("death")
		velocity = Vector2.ZERO
		#hurt = false
	
	
	if velocity.x < 0:
		$Sprite.scale.x = -1
		$Position2D.scale.x = -1
	elif velocity.x > 0:
		$Sprite.scale.x = 1
		$Position2D.scale.x = 1
	velocity = move_and_slide(velocity)


func _on_HurtBox_area_entered(area):
	hurt = true
	hp -= 1
	if hp <= 0:
		die = true
	print(area)
