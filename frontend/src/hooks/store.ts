import { useDispatch as dispatchHook, useSelector as selectorHook} from 'react-redux';
import {AppDispatch, RootState} from '../services/store';


export const useDispatchTyped = dispatchHook.withTypes<AppDispatch>()
export const useSelectorTyped = selectorHook.withTypes<RootState>()
