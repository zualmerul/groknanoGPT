out_dir = "out-shakespeare-char"
eval_interval = 200
eval_iters = 200
# I'm not sure what's going on, but when log_interval == 100, the time per iter is inaccurate and much longer than it should be
# when running on multiple GPUs. TODO: investigate
log_interval = 200  # don't print too too often

always_save_checkpoint = True

wandb_log = True
wandb_project = "grokchess"
wandb_run_name = "2layer_26kgames_1decay_grokfast"

dataset = "tic_tac_toe"
gradient_accumulation_steps = 1
batch_size = 1024
block_size = 26  # context of up to 1023 tokens (because dataset block size is 1024)

# baby GPT model :)
n_layer = 2
n_head = 2
n_embd = 128
dropout = 0.0

learning_rate = 0.00001
max_iters = 100000000
lr_decay_iters = max_iters  # make equal to max_iters usually
min_lr = 3e-5  # learning_rate / 10 usually
beta2 = 0.95  # make a bit bigger because number of tokens per iter is small

warmup_iters = 2000  # not super necessary potentially
compile = True

weight_decay = 1