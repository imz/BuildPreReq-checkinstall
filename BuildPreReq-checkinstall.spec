# Guess whether the girar instance that is building us
# does not actually perform install checks.
#
# This guess can be overridden by: --with/--without install_check_in_girar
#
# * if it's a platform whose "official" girar instance is known (as of now)
# to skip the install checks
%ifarch %e2k
%def_without install_check_in_girar
%endif
# * or--to generalize--if the current build resembles that kind of girar instance
# by having another feature characteristic of the e2k girar,
# namely, --disable check
%if_disabled check
%def_without install_check_in_girar
%endif
%if_without check
%def_without install_check_in_girar
%endif
# * then we switch on the special behavior of our package
# to simulate an install check,
# * else (by default) we switch it off.
# (The %%def_with below won't have an effect if any of the %%def_without above
# have been evaluated.)
%def_with install_check_in_girar
