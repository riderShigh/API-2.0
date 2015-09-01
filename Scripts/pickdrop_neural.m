fields = fieldnames(data); 
xy = [];
champs = [131 134 25 27 28 161 4 8 127 268 55 50 115 117 112 82 84 85 3 7 245 103 101 105 38 31 30 34 60 61 63 68 69 99 90 96 10 13 17 45 43 1 9 143 76 74];

for j = 1:size(champs,2)
    dataFile = strcat('I:\Others\pickDropStats\filtered\',num2str(champs(j)),'.json')
    data = loadjson(dataFile);
    fields = fieldnames(data); 
    for i = 1:numel(fields)
        xy = [xy; data.(fields{i})(1) data.(fields{i})(2)];
    end
end

save('xy.mat','xy')

