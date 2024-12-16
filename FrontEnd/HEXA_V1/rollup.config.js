import path from 'path';
import alias from '@rollup/plugin-alias';

export default {
    plugins: [
        alias({
            entries: [
                {
                    find: '@',
                    replacement: path.resolve(__dirname, 'src/')
                },
            ],
        }),
    ],
};