import { Fragment } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import { IStreamingProvider } from '../interfaces/IStreaming';

interface ProviderModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectProvider: (provider: IStreamingProvider) => void;
}

/**
 * Available streaming providers
 */
const providers: IStreamingProvider[] = [
  { id: 'tamilmv', name: 'TamilMV' },
  { id: 'piratebay', name: 'PirateBay' }
];

/**
 * Modal component for selecting a streaming provider
 */
const ProviderModal = ({ isOpen, onClose, onSelectProvider }: ProviderModalProps) => {
  return (
    <Transition appear show={isOpen} as={Fragment}>
      <Dialog as="div" className="relative z-[999999]" onClose={onClose}>
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-black/50 backdrop-blur" />
        </Transition.Child>

        <div className="fixed inset-0 overflow-y-auto">
          <div className="flex min-h-full items-center justify-center p-4 text-center">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 scale-95"
              enterTo="opacity-100 scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 scale-100"
              leaveTo="opacity-0 scale-95"
            >
              <Dialog.Panel className="w-full max-w-md p-4 text-left align-middle rounded-xl bg-background-light dark:bg-slate-900 shadow-xl transform overflow-hidden transition-all">
                <Dialog.Title className="text-lg font-medium text-slate-900 dark:text-slate-100">
                  Select Provider
                </Dialog.Title>
                <div className="mt-4 space-y-4">
                  {providers.map((provider) => (
                    <button
                      key={provider.id}
                      className="w-full p-3 text-left rounded-md hover:bg-slate-200 dark:hover:bg-slate-800 transition-colors"
                      onClick={() => onSelectProvider(provider)}
                    >
                      <p className="font-medium text-slate-900 dark:text-slate-100">{provider.name}</p>
                    </button>
                  ))}
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition>
  );
};

export default ProviderModal;