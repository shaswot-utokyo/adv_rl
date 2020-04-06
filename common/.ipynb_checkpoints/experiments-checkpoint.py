EXP_PARAMS = {
    'sparse_reward_v3': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9, 
        'batch_size':       32
    },
    'sparse_reward_v2a': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9, 
        'batch_size':       32
    },
    'sparse_reward_v2': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9, 
        'batch_size':       32
    },
    'sparse_reward_v2-high_gamma': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.999, #<<<<<<<
        'batch_size':       32
    },
    'sparse_reward-high_gamma': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.999, #<<<<<<<
        'batch_size':       32
    },
    'sparse_reward': { 
        # derived from basic_env_alpha parameters
        # only end of day rewards using wrappers
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_v2a': { 
        # derived from basic_env_alpha parameters
        # halfing DFACTOR = 0.01
        # NO. of duty cycles = 5
        'env_name':         "basic_env_v2a",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32,
    },
     'basic_env_v2': { 
        # derived from basic_env_alpha parameters
        # halfing DFACTOR to 0.005 from 0.01
        # NO. of duty cycles = 5
        'env_name':         "basic_env_v2",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32,
    },
    'basic_env_v1-high_gamma-b128': { 
        # derived from basic_env_alpha parameters
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "basic_env_v1",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, #<<<
        'batch_size':       128, #<<<<
    },
    'basic_env_v1-high_gamma': { 
        # derived from basic_env_alpha parameters
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "basic_env_v1",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99,#<<<<<
        'batch_size':       32,
    },
    'basic_env_v1': { 
        # derived from basic_env_alpha parameters
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "basic_env_v1",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32,
    },
    'fast_env_alpha-high_gamma-high_LR': { 
        # faster implementation of environment
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "fast_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    5E-3,
        'gamma':            0.99, #< about two days of discounting
        'batch_size':       32
    },
    'fast_env_alpha_high_gamma': { 
        # faster implementation of environment
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "fast_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.99, #< about two days of discounting
        'batch_size':       32
    },
     'fast_env_alpha': { 
        # faster implementation of environment
        # halfing DFACTOR to 0.005 from 0.01
        'env_name':         "fast_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9, #< about 2.5 hours of discounting
        'batch_size':       32
    },
    'basic_env_alpha_b128_8net': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   8, #<<<<
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       128 #<<<<
    },
    'basic_env_alpha_b128': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       128 #<<<<
    },
    'basic_env_alpha-verysmallnet': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   8, #<<<<
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha_double': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          False,#<<<<<
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha_dueling': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         False, #<<<
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha-short_exp-1yrmem': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365, #<<<
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*10, #<<<<
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha-short_exp': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*10, #<<<<
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha-nodd': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         False, #<<<
        'dueling':          False, #<<<<
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2,
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha_small_mem': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*30*6, #replay_size = epsilon_frames
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_alpha': { 
        #smaller net, lower gamma, frequent sync
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, 
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9,
        'batch_size':       32
    },
    'basic_env_small_net': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   32, #<<<
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*30*2, 
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.999,
        'batch_size':       32
    },
    'basic_env_freq_sync': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   128,
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*10, #<<<<
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.999,
        'batch_size':       32
    },
    'basic_env-hi_LR-low_gamma': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   128,
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*30*2,
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    5E-3, #<<<<
        'gamma':            0.9, #<<<<
        'batch_size':       32
    },
    'basic_env_hi_LR': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   128,
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*30*2,
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    5E-3, #<<<<
        'gamma':            0.999,
        'batch_size':       32
    },
    'basic_env_low_gamma': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   128,
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*30*2,
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.9, #<<<<<<
        'batch_size':       32
    },
    'basic_env': {
        'env_name':         "basic_env_v0",
        'double_q':         True,
        'dueling':          True,
        'nn_layer_width':   128,
        'rollout_steps':    1,
        'replay_size':      240*365*2, 
        'replay_initial':   240*10,
        'target_net_sync':  240*30*2,
        'epsilon_frames':   240*30*6,
        'epsilon_start':    1.0,
        'epsilon_final':    0.01,
        'learning_rate':    1E-3,
        'gamma':            0.999,
        'batch_size':       32
    },
}