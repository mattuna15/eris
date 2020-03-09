set -e
#pushd ../assembler >/dev/null
#sh build.sh
#popd >/dev/null
#
pushd scripts >/dev/null
python tables.py
python program.py
#
#python systests.py SimpleVariable
cp basiccode.prg ../../emulator/bin
popd
cp ../kernel/bin/a.lbl generated/kernel.labels
#
python ../assembler/easm.zip 
cp bin/a.prg ../emulator/bin/basic.prg
cp bin/_binary.h ../emulator/bin/_basic.h