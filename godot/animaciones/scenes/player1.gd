extends AnimatedSprite

var speed_walk = 150
var speed_run = 300
var velocity
var anim = "idle"
var first = false

func _process(delta):
	velocity = Vector2.ZERO
	var speed = 0
	
	if Input.is_key_pressed(KEY_SHIFT):
		speed = speed_run
		anim = "run"
	else:
		speed = speed_walk
		anim = "walk"
		
	if Input.is_action_pressed("ui_left"):
		velocity = Vector2.RIGHT * (-speed)
		flip_h = true
	elif Input.is_action_pressed("ui_right"):
		velocity = Vector2.RIGHT * speed
		flip_h = false
	else:
		anim = "idle"
		
	play(anim)
	position += velocity * delta
